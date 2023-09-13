# Logik Version Control and Backup Example

Example support for pulling and pushing of data to and from different Logik environments

- Blueprints

## Github Actions

The sample github actions are configured to be manually triggered, these are provided as a starting point that can be modified further

### Setup

Configure both the Action Variables and the Action Secrets in Github Actions prior to running any of the workflows.

#### Action Variables

- `LOGIK_SOURCE_URL`: Base URL of the source environment that the data is being pulled from
- `LOGIK_DEST_URL`: Base URL of the destination environment that the data is being pushed to

#### Action Secrets

- `LOGIK_SOURCE_API`: Admin API Key for the source environment that the data is being pulled from
- `LOGIK_DEST_API`: Admin API Key for the destination environment that the data is being pushed to

### Running

Manually triggering

### Action inputs

- `NAME`: variable name of the blueprint or managed table to push or pull

#### Pull Actions

Each pull action will export the current data of either the blueprint and create a branch with the new data. The new branch can be compared with the main branch and merged in if desired.

- [Blueprint Pull](.github/workflows/blueprint_pull.yaml)

#### Push Actions

Each push action will create a zip file of either the blueprint from the main branch and start an import job in the destination environment.

- [Blueprint Push](.github/workflows/blueprint_push.yaml)
