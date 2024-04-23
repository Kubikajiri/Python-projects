import pandas as pd

# Globalne ustawienie, aby wyświetlało nam wszystkie kolumny
pd.options.display.max_columns = None

# Zczytanie płatności z uwzględnieniem podzielnika "\" oraz usunięciem wartości NaN
payments = pd.read_csv('C:\\users\\jerzy\OneDrive\\Dokumenty\\GitHub\\Python-projects\\100 Days Python\\Junior Data '
                       'Engineer\\platnosci.csv', sep='\\t', engine='python')
payments.dropna(inplace=True)
# Zczytanie pakietów oraz usunięcie wartości NaN
packages = pd.read_parquet('C:\\Users\\jerzy\\OneDrive\\Dokumenty\\GitHub\\Python-projects\\100 Days Python\\Junior Data Engineer\\pakiety.parquet')
packages.dropna(inplace=True)

# Zmiana nazwy kolumny do późniejszego mergu
packages.rename({'id': 'id_pakietu'}, axis='columns', inplace=True)

#Zczytanie danych pojazdów z usunięciem wartości NaN
vehicles = pd.read_excel('C:\\Users\\jerzy\\OneDrive\\Dokumenty\\GitHub\\Python-projects\\100 Days Python\\Junior Data Engineer\\pojazdy.xlsx', header=None, index_col=None)
vehicles.dropna(inplace=True)
#Zamiana miejscami wiersza 0 i 1 ponieważ nad wierszem tytułowym był dodatkowy wiersz z danymi
vehicles.iloc[0], vehicles.iloc[1] = vehicles.iloc[1], vehicles.iloc[0].copy()

#Ta część kodu odpowiedzialna nest za pozbycie cię nazw "Unnamed 0" oraz "Unnamed 1" w nagłówkach. kod ten bierze pierwszy wiersz i zapisuje go do zmiennej
# new_header, zmienna "vehicles" czyta dane dopiero od 1-go wiersza a nagłówek został nadany od nowa
new_header = vehicles.iloc[0].tolist()
vehicles = vehicles[1:]
vehicles.columns = new_header

vehicles['data_produkcji'] = pd.to_datetime(vehicles['data_produkcji'], errors='coerce', utc=True)
vehicles['data_produkcji'] = vehicles['data_produkcji'].dt.strftime('%Y-%m-%d')
vehicles.rename({'id': 'id_pojazdu'}, axis='columns', inplace=True)

complete_merge = pd.merge(pd.merge(packages, vehicles, on="id_pojazdu", how='outer'), payments, on="id_pojazdu", how='outer')
grouped_table = complete_merge.sort_values(by='id_pojazdu')

#Pytanie 1 - Miesięczna produkcja samochodów:

grouped_table.dropna(inplace=True)

grouped_table['data_produkcji'] = pd.to_datetime(grouped_table['data_produkcji'])
grouped_table['production_month'] = grouped_table['data_produkcji'].dt.month.astype(int)
grouped_table['production_year'] = grouped_table['data_produkcji'].dt.year.astype(int)

monthly_production = grouped_table.groupby(['production_year', 'production_month']).size().reset_index(name='num_cars_produced')
monthly_production = monthly_production.sort_values(by=['production_year', 'production_month'])
print(monthly_production)


#Pytanie 2 - Aktywne pakiety

grouped_table['wartosc_platnosci'] = pd.to_numeric(grouped_table['wartosc_platnosci'], errors='coerce')

active_packages = grouped_table[grouped_table['wartosc_platnosci'] > 0].copy()
# After filtering for active packages
active_packages['pakiet_start'] = pd.to_datetime(active_packages['pakiet_start'], errors='coerce')
active_packages['package_start_month'] = active_packages['pakiet_start'].dt.month.astype(int)
active_packages['package_start_year'] = active_packages['pakiet_start'].dt.year.astype(int)

# Now, group by these columns
monthly_active_packages = active_packages.groupby(['package_start_year', 'package_start_month']).size().reset_index(name='active_packages_count')

# Display the result
print(monthly_active_packages)


# Zadanie 3 - Pakiety nieaktywne

grouped_table['wartosc_platnosci'] = pd.to_numeric(grouped_table['wartosc_platnosci'], errors='coerce')

# Tak jak w przypadku aktywnych pakietów, nieaktywne pakiety mają wartość płatności 0 i tę wartości szukam w tej części kodu
inactive_packages = grouped_table[grouped_table['wartosc_platnosci'] == 0].copy()
inactive_packages['pakiet_start'] = pd.to_datetime(inactive_packages['pakiet_start'], errors='coerce')
inactive_packages['package_start_month'] = inactive_packages['pakiet_start'].dt.month.astype(int)
inactive_packages['package_start_year'] = inactive_packages['pakiet_start'].dt.year.astype(int)

# Zmieniam tutaj typ danych na datetime
inactive_packages.loc[:, 'pakiet_start'] = pd.to_datetime(inactive_packages['pakiet_start'], errors='coerce')

grouped_table['package_start_month'] = grouped_table['pakiet_start'].dt.month.astype(int)
grouped_table['package_start_year'] = grouped_table['pakiet_start'].dt.year.astype(int)

# Create a DataFrame to store the count of active packages for each month
monthly_inactive_packages = inactive_packages.groupby(['package_start_month', 'package_start_year']).size().reset_index(name='inactive_packages_count')

print(monthly_inactive_packages)

#Zadanie 4
grouped_table['data_platnosci'] = pd.to_datetime(grouped_table['data_platnosci'])
grouped_table['data_produkcji'] = pd.to_datetime(grouped_table['data_produkcji'])

# Tutaj zgrupowałem samochody po minimalnej wartości daty płatności co oznacza najwcześniejszą płatność za pakiet
first_payments_per_car = grouped_table.groupby('id_pojazdu')['data_platnosci'].min().reset_index()
print(first_payments_per_car)
# Po zmergowaniu stworzonej wyżej tabeli z oryginalną, mogłem szukać i wyfiltrować tylko najwcześniejsza data
merged_payments = pd.merge(grouped_table, first_payments_per_car, on=['id_pojazdu', 'data_platnosci'], how='inner')

first_payments = merged_payments.drop_duplicates(subset=['id_pojazdu', 'data_platnosci'])
#Tutaj policzyłem płatności ze zmianą daty na częstotliwości miesięczne oraz zrestartowałem indeksowanie kolumn
first_payments_per_month = first_payments.groupby(first_payments['data_platnosci'].dt.to_period('M')).size().reset_index(name='first_payments_count')


print(first_payments_per_month)