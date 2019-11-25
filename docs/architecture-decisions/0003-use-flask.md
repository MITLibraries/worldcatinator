# 3. Use Flask

Date: 2019-11-21

## Status

Accepted

## Context

This application needs to do very little and as such does not need a heavy
framework to succeed.

## Decision

We will use Flask.

## Consequences

Using Flask provides a solution that is appropriate for the scale of application
we will be using, while using Python and Flask which are well understood by
existing engineers in our organization.

There is some risk in that the engineers assigned to this work are not overly
experienced with Flask, but we are comfortable with that level of risk due to
both the size of the application being small and the ability to reach out to
other staff if necessary to overcome any hurdles we may encounter.
