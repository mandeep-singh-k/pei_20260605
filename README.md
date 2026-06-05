## pem interview poc as on 20260605
pei_20260605/
│
├── ddl/                                
│   ├── create_database.sql
│   ├── create_schema.sql
│   ├── create_orders_table.sql
│   ├── create_products_table.sql
│   ├── create_customers_table.sql
│   ├── create_enriched_tables.sql
│   └── create_aggregate_tables.sql
│
├── src/                                
│   ├── data_ingestion.py               
│   ├── transformations.py              
│   ├── aggregations.py                 
│   ├── pipeline_flow.py                
│   └── utils.py                        
│
├── notebooks/
│   └── ecommerce_pipeline.ipynb        
│
├── tests/                              
│   ├── test_ingestion.py
│   ├── test_transformations.py
│   └── test_aggregations.py
│
├── data/                               
│   ├── Orders.json
│   ├── Products.csv
│   └── Customer.xlsx
│
├── requirements.txt                    
├── README.md                           
├── .gitignore                          
└── .github/
    └── workflows/
        └── test.yml                    
