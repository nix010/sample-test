## Installation

To install this project, you can use the following command:
```bash
>> pip install -r requirements
```

Create `.env` file with your information 

```bash
OPENAI_API_KEY=sk-xxx
DATABASE_URL=postgresql://xxx@yyy/database
DATABASE_TEST_URL=postgresql://xxx@yyy/database_test
```

``` bash
>> python seed_data.py

>> python server.py
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [63259] using WatchFiles
INFO:     Started server process [63285]
INFO:     Waiting for application startup
INFO:     Application startup complete.
```

## To run tests

```bash
>> python -m pytest

======================================================================================================== test session starts ========================================================================================================
platform darwin -- Python 3.9.6, pytest-7.4.0, pluggy-1.2.0
rootdir: /Users/khiem_ton/code/docops/sample
plugins: anyio-3.6.2
collected 2 items                                                                                                                                                                                                                   

tests/test_api.py ..                                                                                                                                                                                                          [100%]
=================================================================================================== 2 passed, 1 warning in 11.55s ===================================================================================================

```

## What is completed
- listing api
- Q/A api connect to OpenAI
- Test api at `tests/test_api.py`

## Some improvements can use

- This code is not at prod level.
- Currently the data modeling too simple (just 1).
- Test process not include failed and invalid cases.
- No handling of migration for data schema.
- Haven't finished docker-compose setup yet.
- Don't have diagram for the code yet.

