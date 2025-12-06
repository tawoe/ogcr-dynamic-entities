Dynamic Entities — Tools and Scripts
====================================

Prerequisites
-------------
- Python 3.8+ (use your virtualenv of choice)
```bash
python -m venv .venv
source .venv/bin/activate
```
- Dependencies installed:

```bash
pip install -r requirements.txt
```

Configuration / Environment
---------------------------
The repository includes an example env file. Set the following environment variables (or copy env_example to  `.env`  and load them from `obp_client.py`):

Example (`.env`):

```dotenv
OBP_HOSTNAME=http://localhost:8080
OBP_BANK_ID=mybankid
OBP_USERNAME=myusername
OBP_PASSWORD=mypassword123
OBP_CONSUMER_KEY=35tkq0yksx0lw1sn53kd2jbwonfumgjwssg2jf3g
OBP_LOG_LEVEL=INFO
```


The OGCR Project has received funding from the European Union's Horizon Europe programme under grant agreement 101218854.
