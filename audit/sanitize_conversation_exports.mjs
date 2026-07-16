#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const write = process.argv.includes("--write");

const markdownTargets = [
  "02_CYCLES_PHYSIQUES/ChatGPT-Recherche sur les constantes.md",
  "91_TRAVAUX_ANTERIEURS/ChatGPT-refonte_cadre.md",
  "91_TRAVAUX_ANTERIEURS/Claude-Emotions_modeles_de_langage_et_transcendance_epistemique.md",
  "91_TRAVAUX_ANTERIEURS/Claude-Spontaneous_collapse_models_and_cosmological_time_confusion.md",
  "92_ARCHIVES_CONVERSATIONNELLES/1-ChatGPT-Recherche sur les constantes.md",
  "92_ARCHIVES_CONVERSATIONNELLES/2-ChatGPT-Analyse cohérence projet.md",
  "92_ARCHIVES_CONVERSATIONNELLES/3-ChatGPT-Travail collaboratif projet GitHub.md"
];

const chatGptJsonTargets = [
  "02_CYCLES_PHYSIQUES/ChatGPT-Recherche sur les constantes.json",
  "92_ARCHIVES_CONVERSATIONNELLES/1-ChatGPT-Recherche sur les constantes.json",
  "92_ARCHIVES_CONVERSATIONNELLES/2-ChatGPT-Analyse cohérence projet.json",
  "92_ARCHIVES_CONVERSATIONNELLES/3-ChatGPT-Travail collaboratif projet GitHub.json"
];
const qwenJsonTarget =
  "91_TRAVAUX_ANTERIEURS/QWEN_chat-export-1765463032811.json";

function redactText(value) {
  if (typeof value !== "string") return value;

  return value
    .replace(
      /[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/gi,
      "[ADRESSE_ELECTRONIQUE_RETIREE]"
    )
    .replace(
      /https:\/\/chatgpt\.com\/c\/[A-Za-z0-9-]+/gi,
      "[LIEN_CONVERSATION_RETIRE]"
    )
    .replace(
      /https:\/\/claude\.ai\/(?:chat|chats)\/[A-Za-z0-9-]+/gi,
      "[LIEN_CONVERSATION_RETIRE]"
    )
    .replace(
      /https:\/\/chatgpt\.com\/backend-api\/[^\s)\]>'\"]+/gi,
      "[URL_SIGNEE_RETIREE]"
    )
    .replace(
      /https:\/\/cdn\.qwenlm\.ai\/[^\s)\]>'\"]+/gi,
      "[URL_SIGNEE_RETIREE]"
    )
    .replace(
      /([?&](?:key|token|signature|x-amz-signature)=)[^&\s)\]>'\"]+/gi,
      "$1[VALEUR_RETIREE]"
    )
    .replace(
      /sandbox:\/[^\s)\]>'\"]+/gi,
      "[CHEMIN_TECHNIQUE_RETIRE]"
    )
    .replace(
      /\/workspace\/scratch\/[A-Za-z0-9._\/-]+/gi,
      "[CHEMIN_TECHNIQUE_RETIRE]"
    )
    .replace(
      /[A-Z]:\\Users\\[^\\\s]+(?:\\[^\s,;:()\[\]{}]+)*/gi,
      "[RACINE_LOCALE_ORIGINALE_RETIREE]"
    );
}

function redactMarkdown(source) {
  return redactText(source)
    .replace(/^\*\*User:\*\*.*$/gim, "**User:** [IDENTITE_RETIREE]")
    .replace(/^\*\*Link:\*\*.*$/gim, "**Link:** [LIEN_CONVERSATION_RETIRE]")
    .replace(
      /!\[([^\]]*)\]\(\[(CHEMIN_TECHNIQUE_RETIRE|URL_SIGNEE_RETIREE)\]\)/g,
      "[$1 — $2]"
    )
    .replace(
      /\[([^\]]*)\]\(\[(CHEMIN_TECHNIQUE_RETIRE|URL_SIGNEE_RETIREE)\]\)/g,
      "[$1 — $2]"
    );
}

function sanitizeFirstJson(raw) {
  const source = JSON.parse(raw);
  const metadata = source.metadata ?? {};

  return {
    metadata: {
      title: redactText(metadata.title),
      dates: metadata.dates,
      powered_by: metadata.powered_by,
      sanitization: {
        version: 1,
        removed: [
          "identité et adresse électronique",
          "lien privé de conversation"
        ]
      }
    },
    messages: (source.messages ?? []).map((message) => ({
      role: message.role,
      say: redactText(message.say),
      time: message.time
    }))
  };
}

function pad(number, width) {
  return String(number).padStart(width, "0");
}

function sanitizeQwenJson(raw) {
  const source = JSON.parse(raw);
  if (!source.data && Array.isArray(source.conversations)) return source;

  const conversations = (source.data ?? []).map((conversation, index) => {
    const historyMessages =
      conversation.chat?.history?.messages ?? conversation.chat?.messages ?? {};
    const messages = Array.isArray(historyMessages)
      ? historyMessages
      : Object.values(historyMessages);

    messages.sort((left, right) => {
      const a = Number(left.timestamp ?? 0);
      const b = Number(right.timestamp ?? 0);
      return a - b;
    });

    const localIds = new Map(
      messages.map((message, messageIndex) => [
        message.id,
        `message_${pad(messageIndex + 1, 4)}`
      ])
    );

    return {
      local_id: `conversation_${pad(index + 1, 3)}`,
      title: redactText(conversation.title),
      created_at: conversation.created_at,
      updated_at: conversation.updated_at,
      models: conversation.models ?? conversation.chat?.models ?? [],
      messages: messages.map((message, messageIndex) => ({
        local_id: `message_${pad(messageIndex + 1, 4)}`,
        parent_local_id: localIds.get(message.parentId) ?? null,
        children_local_ids: (message.childrenIds ?? [])
          .map((id) => localIds.get(id))
          .filter(Boolean),
        role: message.role,
        content: redactText(message.content),
        timestamp: message.timestamp,
        models: message.models ?? [],
        edited: Boolean(message.edited),
        attachments: (message.files ?? []).map((file) => ({
          name: redactText(file.name ?? file.file?.filename ?? ""),
          file_type: file.file_type ?? file.file?.meta?.content_type ?? null,
          size: file.size ?? file.file?.meta?.size ?? null
        }))
      }))
    };
  });

  return {
    sanitization: {
      version: 1,
      retained: [
        "titres et horodatages",
        "contenu des messages",
        "rôles et modèles",
        "structure locale des branches",
        "noms, types et tailles des pièces jointes"
      ],
      removed: [
        "identifiants de compte, conversation, message et fichier",
        "identifiants de partage et de requête",
        "URL signées et chemins de téléchargement",
        "configuration technique sans fonction documentaire"
      ]
    },
    conversations
  };
}

function processFile(relativePath, transform) {
  const absolutePath = path.join(root, relativePath);
  if (!fs.existsSync(absolutePath)) return {relativePath, status: "absent"};

  const before = fs.readFileSync(absolutePath, "utf8");
  const after = transform(before);
  const changed = before !== after;

  if (write && changed) fs.writeFileSync(absolutePath, after, "utf8");
  return {relativePath, status: changed ? (write ? "sanitized" : "would-change") : "clean"};
}

const results = [];

for (const relativePath of markdownTargets) {
  results.push(processFile(relativePath, redactMarkdown));
}

for (const relativePath of chatGptJsonTargets) {
  results.push(
    processFile(relativePath, (source) =>
      `${JSON.stringify(sanitizeFirstJson(source), null, 2)}\n`
    )
  );
}
results.push(
  processFile(qwenJsonTarget, (source) =>
    `${JSON.stringify(sanitizeQwenJson(source), null, 2)}\n`
  )
);

for (const result of results) {
  process.stdout.write(`${result.status}\t${result.relativePath}\n`);
}
