import anonimize
import pandas as pd


print(anonimize.importOracleDB())
print(anonimize.anonimize_database(anonimize.importOracleDB()))

