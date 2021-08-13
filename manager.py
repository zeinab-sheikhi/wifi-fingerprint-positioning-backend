import os

from util.db_to_df import export_df_to_csv, sql_table_to_df 

from app import init_app

app = init_app()

if __name__ == "__main__":
    # export_df_to_csv(sql_table_to_df(), '_modified')
    # print('CSV File Exported')
    app.run(host=os.getenv('IP', '192.168.1.3'), port=int(os.getenv('PORT', 3000)), threaded=True)
