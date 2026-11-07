INSERT INTO transactions
(transaction_id, amount, currency, status, reason)
VALUES
(
    'TXN-1042',
    2500.00,
    'KES',
    'FAILED',
    'Insufficient funds'
),
(
    'TXN-1043',
    1200.00,
    'KES',
    'SUCCESS',
    NULL
)
ON CONFLICT (transaction_id) DO NOTHING;