# tsukuru 作る（つくる）

Tsukuru is a vocabulary and concept randomizer application to aid in N5 and N4 JLPT review.

🚧 This project is currently under construction. It already has 2 of the 3 planned components of the monorepo full-stack project, with the frontend underway:

- **Tsukuru** (monorepo) ![Monorepo main-branch version badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fmain%2Fpackage.json&query=version&label) ![Monorepo dev-branch version badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fdev%2Fpackage.json&query=version&label=dev&color=B4CFEC)
- **Kezuru** (data sourcing) ![Kezuru main-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fmain%2Fapps-uv%2Fkezuru%2Fpyproject.toml&query=project.version&label=main&color=08A04B) ![Kezuru dev-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fdev%2Fapps-uv%2Fkezuru%2Fpyproject.toml&query=project.version&label=dev&color=8A9A5B) ![Kezuru kezuru-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fkezuru%2Fapps-uv%2Fkezuru%2Fpyproject.toml&query=project.version&label=kezuru-branch&color=73A16C)
  - [Kezuru data repo](https://github.com/julillermo/kezuru-jlpt-data)

- **Jisho** (backend server) ![Jisho main-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fmain%2Fapps-go%2Fjisho%2Fproject.toml&query=project.version&label=main&color=EDDA74) ![Jisho dev-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fdev%2Fapps-go%2Fjisho%2Fproject.toml&query=project.version&label=dev&color=FAF884) ![Jisho jisho-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fjisho%2Fapps-go%2Fjisho%2Fproject.toml&query=project.version&label=jisho-branch&color=F1E5AC)
- **Kami** (frontend) ![Kami main-branch version badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fmain%2Fapps-ts%2Fkami%2Fpackage.json&query=version&label=main&color=FA8072) ![Kami dev-branch version badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fdev%2Fapps-ts%2Fkami%2Fpackage.json&query=version&label=dev&color=F98B88) ![Kami kami-branch version badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fkami%2Fapps-ts%2Fkami%2Fpackage.json&query=version&label=kami-branch&color=F89880)

## Motivation

- I couldn't find an application specific to the way I want to review Japanese sentence construction, so I made one instead. There is typically a long waiting period leading up to the JLPT exam, and I anticipated difficulty in sustaining Japanese concepts throughout this time. I figured that randomized self-study would be a good approach based on the **"interleaving"** learning strategy. I was hoping to find a dedicated application with a targetted set of **words**, **kanji**, and **concepts** for my **N5/N4** level, but such didn't appear to exist.

### Reason for sourcing from Wikibooks

- The other resources I found previously were mostly publications or materials with **restrictive licensing**. The [Wikibooks JLPT content](https://en.wikibooks.org/wiki/JLPT_Guide), on the other hand, is freely available under the [Creative Commons Attribution-ShareAlike License](https://creativecommons.org/licenses/by-sa/4.0/) as well as having dedicated sections for specific JLPT N-levels.
- I considered using [Jitendex](https://jitendex.org/pages/legal.html), the primary dictionary I use with the [Yomitan](https://github.com/yomidevs/yomitan) project, because it is also under the [Creative Commons Attribution-ShareAlike License](https://creativecommons.org/licenses/by-sa/4.0/). However, I was more interested in an **N5/N4 subset** that also includes **language concepts**, which Wikibooks had. The Wikibooks resource also lends itself more readily to being transformed for instructional material use. Jitendex will instead be used to supplement missing information.

## Quick Start

### 🐳 Run via Docker Compose

The quickest way to try out the project is by running the `compose.self-host.yaml` at the project root via **docker compose**. This ensures that all code runs on an isolated container instead of directly on your system.

1. Install [Docker Desktop](https://docs.docker.com/desktop/) if you intend to run on a **Windows, Mac, or Linux Desktop**, or install [Docker Engine](https://docs.docker.com/engine/) if you intend to run on a **server**. Verify that the following command returns the docker componse version:

```sh
docker compose version # expect something like 'Docker Compose version v2.39.4-desktop.1'
```

2. Clone the Tsukuru repo:

```sh
# Run at your chosen directory
git clone https://github.com/julillermo/tsukuru.git
```

3. Navigate to the Tsukuru project root and run the following command:

```sh
docker compose -f compose.self-hosted.yaml up
```

🎉 Congratulations! You're now running Tsukuru in an isolated container!

Refer to the [Usage](#Usage) section for basics on how to use Tsukuru.

### ♻️ Clean up to free disk space after use

Perform the following steps if you were only intending to try out Tsukuru short-term. In your **Docker Desktop** application, do the following:

1. Head to the **Containers** tab and delete everything under (and including) tsukuru. You'll see something like the following.
   - `postgresql-1`
   - `feed-1`
   - `jisho-1`
2. Head to the **Images** tab and delete everything tsukuru-related. You'll likely see the following (~750 MB):
   - `tsukuru-jisho`
   - `tsukuru-feed`
3. Head to the **Volumes** tab and delete everything tsukuru-related. You'll likely see the following:
   - `tsukuru_feed_state`
   - `tsukuru_postgres_data`

🧹 All done! You now no longer have any tsukuru-related files besides the repo copy.

## Usage

The **frontend** for Tsukuru is currently **under construction**, but you can already get the general idea of the app by trying out the primary API of the project. Run the following CURL command and test out different values for `concepts` and `vocabs` to your liking 🤓.

```sh
curl --request GET \
  --url 'http://localhost:8081/tsukuru/constructs/random?concepts=2&vocabs=5'
```

Example Output:

```json
{
  "vocabularies": [
    {
      "id": "0c7f3da4-55fa-4da3-aa80-249273162dc5",
      "jlpt_level": "n5",
      "wiki_index": 347,
      "kana_writing": "~だい",
      "kanji": "~台",
      "classification": ["suffix"],
      "definition": "counter for vehicles"
    },
    {
      "id": "d3f45eff-8dae-41d5-889a-126e9edcee5e",
      "jlpt_level": "n5",
      "wiki_index": 326,
      "kana_writing": "せまい",
      "kanji": "狭い",
      "classification": ["adjective"],
      "definition": "narrow, confined, small"
    }
  ],
  "grammar_concepts": [
    {
      "created_at": "2026-09-05T22:56:32Z",
      "updated_at": "2026-09-05T22:56:32Z",
      "id": "efe52b3c-9ae8-42ce-9cb8-528ba53e4ada",
      "jlpt_level": "n5",
      "concept": "と",
      "definition": "This is a particle used to link nouns in a complete list.",
      "examples": [
        {
          "id": "4218e782-310c-4db7-9e06-b09929383653",
          "grammar_concept_id": "",
          "japanese_text": "そのサラダはレタスと にんじん と ラディッシュから　作り（つくり）ました。",
          "english_meaning": "The salad was made from lettuce, carrot, and radish."
        }
      ]
    },
    {
      "created_at": "2026-09-05T22:56:32Z",
      "updated_at": "2026-09-05T22:56:32Z",
      "id": "041e9b80-1d13-4b88-95e9-5a51bf06a34f",
      "jlpt_level": "n4",
      "concept": "～のような",
      "definition": "This pattern acts as an adjective for describing nouns.",
      "examples": [
        {
          "id": "9225a902-b645-49bb-bddc-9f67cacce5c3",
          "grammar_concept_id": "",
          "japanese_text": "ある意味（いみ）で、スージーは私（わたし）のお母（おかあ）さんのような ものだ。",
          "english_meaning": "In a way, Susie seems like my mother."
        },
        {
          "id": "d9043109-8e88-4f59-a270-b2a84525bf5c",
          "grammar_concept_id": "",
          "japanese_text": "貴方（あなた）は天使（てんし）のような 子（こ）だ。",
          "english_meaning": "You are an angel of a child."
        }
      ]
    }
  ]
}
```

## Contributing

- There are no specific rules on how to contribute at the moment, so feel free to contribute in any way possible, especially with bug reports 😁.
