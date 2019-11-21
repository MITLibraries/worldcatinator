# 2. Do as little as possible in Aleph

Date: 2019-11-21

## Status

Accepted

## Context

The problem space allows for solutions to be completed in various ways. This
decision documents the overall approach to how we will build a solution while
providing context as to what decisions

We are tasked with creating links to WorldCat from a specific Aleph page. The
page we need to work with does not have access to the OCLC number which we need
to make a link into WorldCat, so an API lookup will be necessary to get the
data we need.

The TIMDEX! API has access to the metadata we need and the Aleph page has access
to the Identifier necessary to make the API call.

The Aleph page has a lot of custom, inline JavaScript that is currently not
under version control and has no automated tests or automated deployment
process.

## Decision

We will do as little as possible in Aleph.

We will use JavaScript in Aleph to
generate HTML containing links to a custom application that will call TIMDEX
to get data we need and issue a redirect to WorldCat. If the TIMDEX API does
not have data for the record for some reason that we need, we will redirect to a
generic link in WorldCat.

This application will never render any HTML to the end user and will
only ever provide redirects.

## Consequences

This allows for building a well tested solution using modern code and deployment
processes. This prevents us from having to manually move code into place for the
bulk of the functionality. This will allow for automated tests, automated
deployments, excpeption monitoring, and centralized logging following our normal
Engineering practices.

Only the relatively small portion of creating a link and inserting it into the
DOM will be done in Aleph.
