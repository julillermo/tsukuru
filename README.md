# tsukuru 作る（つくる）

Tsukuru is a vocabulary and concept randomizer application to aid in N5 and N4 JLPT review.

🏗️ This project is currently under construction. It is planned to have 3 components that coordinate as a full-stack project:

- **Tsukuru** (monorepo) ![Mono repo version badge](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fmain%2Fpackage.json&query=version&label=main)
- **Kezuru** (data sourcing) ![Kezuru main-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fmain%2Fapps-uv%2Fkezuru%2Fpyproject.toml&query=project.version&label=main) ![Kezuru dev-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fdev%2Fapps-uv%2Fkezuru%2Fpyproject.toml&query=project.version&label=dev&color=pink) ![Kezuru kezuru-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fkezuru%2Fapps-uv%2Fkezuru%2Fpyproject.toml&query=project.version&label=kezuru-branch&color=white)
  - [Kezuru data repo](https://github.com/julillermo/kezuru-jlpt-data)

- **Jisho** (backend server) ![Jisho jisho-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fmain%2Fapps-go%2Fjisho%2Fproject.toml&query=project.version&label=main) ![Jisho dev-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fdev%2Fapps-go%2Fjisho%2Fproject.toml&query=project.version&label=dev&color=pink) ![Jisho jisho-branch version badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjulillermo%2Ftsukuru%2Fjisho%2Fapps-go%2Fjisho%2Fproject.toml&query=project.version&label=jisho-branch&color=white)
- **Kami** (frontend) ![Kami status](https://img.shields.io/badge/status-planned-yellow)

## Motivation

- I couldn't find an application specific to the way I want to review Japanese sentence construction, so I made one instead. There is typically a long waiting period leading up to the JLPT exam, and I anticipated difficulty in sustaining Japanese concepts throughout this time. I figured that randomized self-study would be a good approach based on the "interleaving" learning strategy. I was hoping to find a dedicated application with a targetted set of words, kanji, and concepts for my N5/N4 level, but such didn't appear to exist.

<!-- TODO Likely move to a more specific location instead of the README later on-->

### Reason for sourcing from Wikibooks

- The other resources I found previously were mostly publications or materials with restrictive licensing. The [Wikibooks JLPT content](https://en.wikibooks.org/wiki/JLPT_Guide), on the other hand, is freely available under the [Creative Commons Attribution-ShareAlike License](https://creativecommons.org/licenses/by-sa/4.0/) as well as having dedicated sections for specific JLPT N-levels.
- I considered using [Jitendex](https://jitendex.org/pages/legal.html), the primary dictionary I use with the [Yomitan](https://github.com/yomidevs/yomitan) project, because it is also under the [Creative Commons Attribution-ShareAlike License](https://creativecommons.org/licenses/by-sa/4.0/). However, I was more interested in an N5/N4 subset that also includes language concepts, which Wikibooks had. The Wikibooks resource also lends itself more readily to instructional material use. Jitendex will instead be used to supplement missing information.

## Quick Start

- TBA

## Usage

- TBA

## Contributing

- There are no specific rules for contributing at the moment, so feel free to contribute in any way possible, especially with bug reports 😁.
