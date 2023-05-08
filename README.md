# RMS-RATES

Service to __SERVICE_SUMMARY__.

## SETUP

### LOAD YOUR SERVICE ACCOUNT KEY FILE.

```bash
# linux
export GOOGLE_APPLICATION_CREDENTIALS=/home/user/path/to/service_account_dev.json
echo $GOOGLE_APPLICATION_CREDENTIALS
```

### SETUP YOUR VENV

```bash
# linux
python -m venv .venv
source .venv/bin/activate
```

### INSTALL REQUIREMENTS ON YOUR VENV

```bash
pip install --ignore-installed --no-cache-dir -r requirements.txt
```

## REQUIREMENTS

```coffee
# Cargamos
git+https://bitbucket.org/cargamos/cdp-presentation-python.git@master
rms-domain-python @ git+https://bitbucket.org/cargamos/rms-domain-python.git@v0.0.18#egg=rms-domain-python
logistics-python @ git+https://bitbucket.org/cargamos/logistics-python.git@v1.3.2#egg=logistics-python

```

## RESOURCES

ENDPOINT | METH
--|--
`/v1/rms/batch/rates/rate-vehicles/` | `PATCH`
`/v1/rms/batch/rates/rate-vehicles/` | `POST`
`/v1/rms/rate-vehicles/` | `GET`
`/v1/rms/rate-vehicles/` | `PATCH`
`/v1/rms/rate-vehicles/` | `POST`
`/v1/rms/rates/<string:rate_id>/dcs/<string:dc_id>` | `DELETE`
`/v1/rms/rates/<string:rate_id>/rate-vehicles` | `GET`
`/v1/rms/rates/` | `GET`

## CREATE REAMDE.MD

To download 'auto_docs.py', run the following commands:

```shell
python -c 'from logistics.auto_docs.setup import AutoDocs; AutoDocs.create_auto_docs_file()'
```

Then, from your venv, run python `auto_docs.py` file to generate the README.md file. Basic usage:

```shell
python auto_docs.py -d ./README.md
```

> More details `python auto_docs.py -h`


# ACKNOWLEDGMENTS

Thanks to all cargamos team.

---

* Powered by [xide](mailto:isaias.xicale@cargamos.com) 😎