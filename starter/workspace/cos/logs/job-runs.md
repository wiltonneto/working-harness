# External job run ledger

This deliberately starts empty. No jobs are installed or have run on behalf of this starter. An external runner configured later owns serialized writes here; model jobs write their distinct output files and do not edit this ledger directly. The existing register helper does not implement this ledger's writer.

| Job / run / attempt ID | Contract / config / baseline | Started | Finished | State | Output / evidence | Usage / limit | Recovery owner / next action |
| --- | --- | --- | --- | --- | --- | --- | --- |

See the [runner configuration contract](../system/jobs/README.md) for STARTED/terminal records, incomplete or missing results, all-attempt usage, serialization, and retry handling. Absence of a row is not proof of no execution. Do not fill this table with fictional successful runs.
