# parquet-reader

A small, interactive CLI tool to explore `.parquet` files directly in the terminal – no Jupyter, no GUI, just efficient data inspection.

## Features

- Load a `.parquet` file and list all columns with numeric indices
- Interactively select columns via keyboard input
- Display a random sample of the selected columns
- Optionally export the selection as a CSV file (`auswahl.csv`)

## Installation

### With Poetry (recommended)

```bash
git clone https://github.com/FabioKn/parquet-reader.git
cd parquet-reader
poetry install
```

##  Usage

```bash
poetry run parquet-reader path/to/your/file.parquet
```

You will be presented with a numbered list of all columns. Simply enter the numbers of the columns you want to preview (separated by spaces), and a sample of 5 rows will be displayed.

If desired, the selected data can be saved as `auswahl.csv`.

## Example Output

```bash
Available columns:

 0: id
 1: url
 2: timestamp
 3: content_length

Enter the numbers of the columns to display (space-separated):
>> 0 2 3

Selected columns (sample):

      id         timestamp  content_length
  12345  2023-10-05T10:00Z          182934
  ...
```

## Dependencies

- `pandas`
- `pyarrow`

These will be installed automatically when using Poetry.

## License

This project is licensed under the **European Union Public License (EUPL) v1.2**.  
For more information, see [https://joinup.ec.europa.eu/collection/eupl](https://joinup.ec.europa.eu/collection/eupl).

---

Feel free to open an issue or contribute via pull requests. Feedback and improvements are very welcome!
