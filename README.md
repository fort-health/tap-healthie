# tap-healthie

`tap-healthie` is a Singer tap for Healthie.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Overview

This tap currently supports:

* Appointment Types
* CPT Codes
* ICD10 Codes
* Users (clients)
  * Appointments
  * Charting Items
    * Form Answer Groups
      * Auto-scored Sections
      * Charting Note Addendums
      * Form Answer Group Signings
      * Form Answers
* Organization Members

## Configuration

### Accepted Config Options

<!--
Developer TODO: Provide a list of config options accepted by the tap.

This section can be created by copy-pasting the CLI output from:

```
tap-healthie --about --format=markdown
```
-->

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| environment         | False    | None    | The name of the environment, 'Sandbox' or 'Production' |
| sandbox_api_key     | False    | None    | The Sandbox API Key for authenticating to Healthie's API service |
| production_api_key  | False    | None    | The Production API Key for authenticating to Healthie's API service |
| start_date          | False    | None    | The earliest record date to sync |
| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. |

A full list of supported settings and capabilities is available by running: `tap-healthie --about`

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

<!--
Developer TODO: If your tap requires special access on the source system, or any special authentication requirements, provide those here.
-->

## Usage

<!--
Developer TODO: Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

## Installation

Install from PyPi:

```bash
pipx install tap-healthie
```

Install from GitHub:

```bash
pipx install git+https://github.com/ORG_NAME/tap-healthie.git@main
```
-->

You can easily run `tap-healthie` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-healthie --version
tap-healthie --help
tap-healthie --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-healthie` CLI interface directly using `poetry run`:

```bash
poetry run tap-healthie --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-healthie
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-healthie --version
# OR run a test `elt` pipeline:
meltano elt tap-healthie target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
