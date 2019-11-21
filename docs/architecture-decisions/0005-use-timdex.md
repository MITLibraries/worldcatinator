# 5. Use TIMDEX

Date: 2019-11-21

## Status

Accepted

## Context

Their are multiple ways to get the metadata needed (the OCLC number) based on
the Aleph ID (also knows as the `doc_id`, `identifier`, `bibid` depending on
who you are talking to).

Options include:

- Aleph XML API
- Z39.50
- TIMDEX!

## Decision

We will use TIMDEX!

## Consequences

TIMDEX! is our most modern and developer friendly option for this work.

Using it will help prove it is a production level service and help us feel more
confident in pointing others to use it as well.
