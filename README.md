# worldcatinator (formerly renorect: RENOvation rediRECT)

## What is this?

This application takes a supplied MIT Aleph Bibid, looks up an OCLC number
in the Bib Record via TIMDEX! and redirects the requestor to our WorldCat
page for the record.

If no Bibid is supplied, no record is found, or no OCLC numbers are found,
the requestor is sent to our generic WorldCat page.

This is intended to provide a way to link from our Aleph records during the
renovation of Hayden library and will be retired as soon as that is complete.

The code to insert links into the Aleph records is not included in this
repository.

## Development

Clone the repo and install the dependencies using [Pipenv](https://docs.pipenv.org/):

```shell
git clone git@github.com:MITLibraries/worldcatinator.git

cd worldcatinator

pipenv shell

pipenv install
```

## Docker

To build and run in docker:

```bash
docker build -t worldcatinator .

docker run -it -p 5000:5000 worldcatinator
```

## Environment Variables

- `SENTRY_DSN` (optional). If set to a valid value (obtain from Sentry),
  exceptions will be sent to Sentry
- `TIMDEX_URL` (default is to production TIMDEX). Set to stage, PR or local
  TIMDEX endpoint if you have reason to do so
