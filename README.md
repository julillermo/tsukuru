# tsukuru 作る（つくる）

Tsukuru is a vocabulary and concept randomizer application to aid in N5 and N4 JLPT review.

🚧 This project is currently under construction. It already has 2 of the 3 planned components of the monorepo full-stack project, with the frontend underway:

- **Tsukuru** (monorepo) ![Monorepo main-branch version badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fmain%2Fpackage.json&query=version&label=main) ![Monorepo dev-branch version badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fdev%2Fpackage.json&query=version&label=dev&color=pink)
- **Kezuru** (data sourcing) ![Kezuru main-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fmain%2Fapps-uv%2Fkezuru%2Fpyproject.toml&query=project.version&label=main) ![Kezuru dev-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fdev%2Fapps-uv%2Fkezuru%2Fpyproject.toml&query=project.version&label=dev&color=pink) ![Kezuru kezuru-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fkezuru%2Fapps-uv%2Fkezuru%2Fpyproject.toml&query=project.version&label=kezuru-branch&color=white)
  - [Kezuru data repo](https://github.com/julillermo/kezuru-jlpt-data)

- **Jisho** (backend server) ![Jisho jisho-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fmain%2Fapps-go%2Fjisho%2Fproject.toml&query=project.version&label=main) ![Jisho dev-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fdev%2Fapps-go%2Fjisho%2Fproject.toml&query=project.version&label=dev&color=pink) ![Jisho jisho-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fjisho%2Fapps-go%2Fjisho%2Fproject.toml&query=project.version&label=jisho-branch&color=white)
- **Kami** (frontend) ![Kami status](https://img.shields.io/badge/status-planned-yellow)

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

The **frontend** for Tsukuru is currently **under construction**, but you can already get the general idea of the appl by trying out the primary API of the project. Run the following CURL command and test out different values for `concepts` and `vocabs` to your liking 🤓.

```sh
curl --request GET \
  --url 'http://localhost:8081/tsukuru/constructs/random?concepts=2&vocabs=5'
```

Example Output:

```json
{
  "vocabularies": [
    {
      "id": "a15c5bc1-8899-4cb0-bba3-e9328cd29961",
      "jlpt_level": "n4",
      "wiki_index": 246,
      "kana_writing": "さいきん",
      "kanji": "最近",
      "classification": [],
      "definition": "recently"
    },
    {
      "id": "15997a40-6374-4257-8dcd-fed0942fdfc8",
      "jlpt_level": "n4",
      "wiki_index": 375,
      "kana_writing": "たずねる",
      "kanji": "",
      "classification": [],
      "definition": "to visit, to pay a visit to"
    },
    {
      "id": "2eb31b2d-2f5e-4c58-8f92-ab112ec6fbd0",
      "jlpt_level": "n4",
      "wiki_index": 597,
      "kana_writing": "ゆ",
      "kanji": "",
      "classification": ["noun"],
      "definition": "steam"
    }
  ],
  "grammar_concepts": [
    {
      "id": "95b03cee-33d7-450d-9b8a-33d46ac5ec28",
      "jlpt_level": "n4",
      "concept": "～ておく",
      "definition": "It means to do something in advance."
    },
    {
      "id": "102eaae5-6a24-4fa2-95c1-8c0841577faf",
      "jlpt_level": "n5",
      "concept": "～まえに",
      "definition": "It means \"before doing (something)\" or \"ago\" (like 3 days ago)."
    }
  ]
}
```

## Contributing

- There are no specific rules on how to contribute at the moment, so feel free to contribute in any way possible, especially with bug reports 😁.
