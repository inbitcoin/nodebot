
def cmds():
    getinfo = '{"identity_pubkey":"0229bfbea3f31a9b720b9da68e20b53c692860769e446f25daba27f6e9e045ea63","alias":"B Boo","num_pending_channels":0,"num_active_channels":3,"num_peers":7,"block_height":527017,"block_hash":"0000000000000000002072fd092dd211519cff013a46c9ba216df1899f344ce8","synced_to_chain":true,"testnet":false,"chains":["bitcoin"],"uris":["0229bfbea3f31a9b720b9da68e20b53c692860769e446f25daba27f6e9e045ea63@93.40.7.67:9735"],"best_header_timestamp":"1528740387","version":"0.4.2-beta commit=7cf5ebe2650b6798182e10be198c7ffc1f1d6e19"}'
    # payinvoice = '{"payment_error":"unable to find a path to destination","payment_preimage":"","payment_route":null}'
    payinvoice = '{"payment_error":"","payment_preimage":"d395f4966b9ab34219e6d22676127562c67d59d9f3138a6fa834500a325ee378","payment_route":{"total_time_lock":527561,"total_fees":1,"total_amt":149,"hops":[{"chan_id":579098480736010241,"chan_capacity":592440,"amt_to_forward":148,"fee":1,"expiry":527417,"amt_to_forward_msat":148002,"fee_msat":1118},{"chan_id":572939016663203840,"chan_capacity":1000000,"amt_to_forward":148,"expiry":527273,"amt_to_forward_msat":148000,"fee_msat":2},{"chan_id":579319482654392320,"chan_capacity":1000000,"amt_to_forward":148,"expiry":527273,"amt_to_forward_msat":148000}],"total_fees_msat":1120,"total_amt_msat":149120}}'
    addinvoice = '{"r_hash":"bcb1cc2cca6a26bf0d2ba86ed4dc09b64d45ccecff663819eb56ab5477481ed6","pay_req":"lnbc1pd3aml7pp5hjcuctx2dgnt7rft4phdfhqfkex5tn8vlanrsx0t2644ga6grmtqdqqcqzyshxnsetaufstvawr83yq6st9kjk072d2yp7cu4dawyc36ac05rva9ar7mmt8mldg3v56krx80jp7rdycrxjcz9qea6z4t3dvm2aan8xgpu7ey67"}'
    walletbalance = '{"total_balance":"4336765","confirmed_balance":"4336765","unconfirmed_balance":"0"}'
    channelbalance = '{"balance":"1128190","pending_open_balance":"0"}'
    listchannels = '{"channels":[{"active":true,"remote_pubkey":"024a2e265cd66066b78a788ae615acdc84b5b0dec9efac36d7ac87513015eaf6ed","channel_point":"b4e296e1bac367a09b3c650efe2c24627235ffa2f096c0f9d6aa2d454f17a57b:1","chan_id":"579098480736010241","capacity":"600000","local_balance":"598552","remote_balance":"0","commit_fee":"1448","commit_weight":"600","fee_per_kw":"2000","unsettled_balance":"0","total_satoshis_sent":"0","total_satoshis_received":"0","num_updates":"49","pending_htlcs":[],"csv_delay":144,"private":false},{"active":true,"remote_pubkey":"03557fd11b58cb93d2ad4fab4dd4cff7462a97e21e8f6b7a712cb8bd27a96b9eef","channel_point":"4d378dac54b153b13c03d2d0b3068c5c754df17c762215ea1c9a340ab9ed55a6:0","chan_id":"579098480736075776","capacity":"500000","local_balance":"498552","remote_balance":"0","commit_fee":"1448","commit_weight":"600","fee_per_kw":"2000","unsettled_balance":"0","total_satoshis_sent":"0","total_satoshis_received":"0","num_updates":"51","pending_htlcs":[],"csv_delay":144,"private":false},{"active":false,"remote_pubkey":"036fd87befd85ea3f2b0c4e687757b7acb257c44758681e3a9b657776b34da8f64","channel_point":"ca53a8942d4fddf2384051a3ddd5404a121ee03e02cf71b2432f27dbc100428c:1","chan_id":"579129267098681345","capacity":"100000","local_balance":"30000","remote_balance":"68552","commit_fee":"1448","commit_weight":"724","fee_per_kw":"2000","unsettled_balance":"0","total_satoshis_sent":"0","total_satoshis_received":"0","num_updates":"18","pending_htlcs":[],"csv_delay":144,"private":false},{"active":true,"remote_pubkey":"03c2d52cdcb5ddd40d62ba3c7197260b0f7b4dcc29ad64724c68426045919922f0","channel_point":"53f2daff7a479e40ae6abc43e3668f56c28d2520616f60a02c34449ebcb99ccf:0","chan_id":"579135864171397120","capacity":"50000","local_balance":"0","remote_balance":"49276","commit_fee":"724","commit_weight":"552","fee_per_kw":"1000","unsettled_balance":"0","total_satoshis_sent":"0","total_satoshis_received":"0","num_updates":"44","pending_htlcs":[],"csv_delay":144,"private":false},{"active":true,"remote_pubkey":"03db61876a9a50e5724048170aeb14f0096e503def38dc149d2a4ca71efd95a059","channel_point":"bda12a4773ee81c6644ec1573a802f0b63011dc450660d876ac99eb15b38cebe:0","chan_id":"579657032674181120","capacity":"700000","local_balance":"698552","remote_balance":"0","commit_fee":"1448","commit_weight":"600","fee_per_kw":"2000","unsettled_balance":"0","total_satoshis_sent":"0","total_satoshis_received":"0","num_updates":"0","pending_htlcs":[],"csv_delay":144,"private":false}]}'
    describegraph = '{"nodes":[{"last_update":1528852475,"pub_key":"0229bfbea3f31a9b720b9da68e20b53c692860769e446f25daba27f6e9e045ea63","alias":"B Boo","addresses":[{"network":"tcp","addr":"93.40.7.67:9735"}],"color":"#004bbc"},{"last_update":1528852502,"pub_key":"03db61876a9a50e5724048170aeb14f0096e503def38dc149d2a4ca71efd95a059","alias":"mani_al_cielo","addresses":[],"color":"#ff0000"},{"last_update":1517355924,"pub_key":"02006b7be7ea4b7cdf181c5c7b338e80904f13173220eb07e991a268e518a35b4a","alias":"SILKROUTE","addresses":[{"network":"tcp","addr":"81.83.154.157:9735"}],"color":"#02006b"}],"edges":[{"channel_id":"555122530222276608","chan_point":"ab3ed05032302c2672b77cb58f9b5128b8e9451c65b72b2cf3318548b8a4874e:0","last_update":1528509169,"node1_pub":"02c0ac82c33971de096d87ce5ed9b022c2de678f08002dc37fdb1b6886d12234b5","node2_pub":"02ee4469f2b686d5d02422917ac199602ce4c366a7bfaac1099e3ade377677064d","capacity":"250000","node1_policy":{"time_lock_delta":14,"min_htlc":"1000","fee_base_msat":"1000","fee_rate_milli_msat":"1"},"node2_policy":{"time_lock_delta":144,"min_htlc":"0","fee_base_msat":"1000","fee_rate_milli_msat":"1"}}]}'
    decodepayreq = '{"destination":"0229bfbea3f31a9b720b9da68e20b53c692860769e446f25daba27f6e9e045ea63","payment_hash":"5cb50915e0fc70701cdc81c0d57a896e725f099009b77ea372d5500ac40a4662","num_satoshis":"1000000","timestamp":"1528898241","expiry":"3600","description":"","description_hash":"","fallback_addr":"","cltv_expiry":"144","route_hints":[]}'
    feereport = '{"channel_fees":[{"channel_point":"b4e296e1bac367a09b3c650efe2c24627235ffa2f096c0f9d6aa2d454f17a57b:1","base_fee_msat":"1000","fee_per_mil":"1","fee_rate":1e-06},{"channel_point":"4d378dac54b153b13c03d2d0b3068c5c754df17c762215ea1c9a340ab9ed55a6:0","base_fee_msat":"1000","fee_per_mil":"1","fee_rate":1e-06},{"channel_point":"bda12a4773ee81c6644ec1573a802f0b63011dc450660d876ac99eb15b38cebe:0","base_fee_msat":"1000","fee_per_mil":"1","fee_rate":1e-06},{"channel_point":"a3dbdf1666f9b80ae232682d357446c787815246b7dcae7135fb824b3a1f3215:0","base_fee_msat":"1000","fee_per_mil":"1","fee_rate":1e-06}],"day_fee_sum":"2","week_fee_sum":"2","month_fee_sum":"4"}'
    error = '[lncli] rpc error: code = Unknown desc = payment of 1.2 BTC is too large, max payment allowed is 0.04294967 BTC'

    return locals()
