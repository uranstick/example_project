# Update transaction status

**URL**

/api/dashboard/transactions/

**Method**

POST

**Request example**

```json
{
    "transactions": [
        1, 2, 3
    ],
    "status": "BATCHING"
}
```
Valid options for status: ["BATCHING", "COINS_SENT", "COMPLETE", "DUPLICATE"]

# Transactions list

**URL**

/api/dashboard/transactions/

**Method**

GET

**URL Params**

Param | Description
--- | --- 
page | page of results to return, 1000 transactions per page
status | filter transactions by status, might be one of the following ["RECEIVED", "BATCHING", "SENT_TO_WALLET", "COINS_SENT", "COMPLETE", "DUPLICATE"]
address | filter transactions by address
internal_transaction_id | filter transactions by internal_transaction_id
blockchain_transaction_id | filter transactions by blockchain_transaction_id
coin_amount | filter transactions by coin_amount
coin_amount__lt | filter transactions with coin_amount lower than value
coin_amount__gt | filter transactions with coin_amount greater than value
created__lt | filter transactions with created datetime lower than value, date format '%Y-%m-%d %H:%M:%S'
created__gt | filter transactions with created datetime greater than value, date format '%Y-%m-%d %H:%M:%S'
updated__lt | filter transactions with updated datetime lower than value, date format '%Y-%m-%d %H:%M:%S'
updated__gt | filter transactions with updated datetime greater than value, date format '%Y-%m-%d %H:%M:%S'

**Response**

```json
{
    "count":1000,
    "next":"{DOMAIN}/api/dashboard/transactions/?page=2",
    "previous":null,
    "results":[
        {
            "id":7,
            "created":"2021-02-24T15:16:24.227007Z",
            "updated":"2021-02-24T15:16:24.227025Z",
            "coin_type":"btc",
            "coin_amount":5207,
            "address":"11yEmxiMso2RsFVfBcCa616npBvGgxiBX",
            "blockchain_transaction_id":null,
            "internal_transaction_id":"luxtlxrkfllff0g3qvtkv317vn7e3yxxv1zwx7n1uyxce57x8zhyqur4tm0jfue8",
            "status":"COMPLETE"
        },
        ...
    ]
}
```
# Transaction detail

**URL**

/api/dashboard/transactions/{id}

**Method**

GET

**Response**

```json
{
    "id":5,
    "created":"2021-02-24T15:15:38.960700Z",
    "updated":"2021-02-24T15:15:38.960718Z",
    "coin_type":"btc",
    "coin_amount":5569,
    "address":"11yEmxiMso2RsFVfBcCa616npBvGgxiBX",
    "blockchain_transaction_id":null,
    "internal_transaction_id":"luxwobs0kmz1cb10kgd7r3k5ysz8oda285lf2lkge1joitmwp12jnq46i1ughgsc",
    "status":"DUPLICATE"
}
```

# Batching settings

**URL**

/api/dashboard/batching_settings_peak/

**Method**

GET | POST

**Request example**

```json
{
    "peak_batching_time":900,
    "offpeak_batching_time":2400,
    "peak_hour_start":7,
    "peak_hour_end":21,
    "batching_amount":50000,
    "send_to_bitgo":true
}
```
**Notes**

'peak_batching_time' and 'offpeak_batching_time' should be greater than settings.MIN_BATCHING_INTERVAL_SECONDS (60 seconds).
'peak_hour_start' must be earlier than 'peak_hour_end'

**Response**

```json
{
    "batching_time":900,
    "peak_batching_time":900,
    "offpeak_batching_time":2400,
    "peak_hour_start":7,
    "peak_hour_end":21,
    "batching_amount":50000,
    "send_to_bitgo":true
}
```
