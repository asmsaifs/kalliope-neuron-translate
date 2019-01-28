# Translate

## Synopsis

Neuron to translate sentence with google API

## Installation

```bash
kalliope install --git-url https://github.com/asmsaifs/kalliope-neuron-translate.git
```

## Options

| parameter | required | default | choices                                | comments                                                                         |
|-----------|----------|---------|----------------------------------------|----------------------------------------------------------------------------------|
| lang_out  | yes      |         | E.g: "en", "bn", "Spanish", "Français" | Language to translate sentence: langage code ("bn") or language name ("Spanish") |
| lang_in   | yes      |  auto   | E.g: "auto", "en", "bn"                | Language of original sentence: "auto" for automatique detection or lang code     |
| sentence  | yes      |         |                                        | Sentence translate                                                               |

[Langage support and ISO-639-1 Code](https://cloud.google.com/translate/docs/languages) 

## Return Values

| Name     | Description           | Type   | sample          |
|----------|-----------------------|--------|-----------------|
| result   | Result of translation | string | "Buenas noches" |
| lang_in  | lang id in            | string | "bn"            |
| lang_out | lang id out           | string | "en"            |

## Synapses example with override voice parameter

```yml
- name: "translate-bn"
  signals:
    - order: "{{sentence}} এর ইংরেজি কি"
  neurons:
    - translate:
        lang_in: "bn"
        lang_out: "en"
        sentence: "{{sentence}}"
        say_template: 
          - "{{ result }}"
        tts:             
          googletts:
            language: "en"
            cache: False
```
