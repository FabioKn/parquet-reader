def main(): 
    import pandas as pd
    import pyarrow.parquet as pq
    import argparse
    
    # Argumente einlesen
    parser = argparse.ArgumentParser(description="Parquet-Datei interaktiv untersuchen")
    parser.add_argument("parquet_file", help="Pfad zur .parquet-Datei")
    args = parser.parse_args()
    
    # Parquet-Datei laden
    try:
        table = pq.read_table(args.parquet_file)
    except Exception as e:
        print(f"Fehler beim Laden der Datei: {e}")
        exit(1)
    
    df = table.to_pandas()
    
    # Spalten nummeriert anzeigen
    print("Verfügbare Spalten:\n")
    for i, col in enumerate(df.columns):
        print(f"{i:2d}: {col}")
    
    # Eingabe für Spaltenauswahl
    print("\nGib die Nummern der Spalten ein, die du anzeigen möchtest (getrennt durch Leerzeichen):")
    selection = input(">> ")
    
    # Eingabe verarbeiten
    try:
        selected_indices = [int(i) for i in selection.strip().split()]
        selected_columns = [df.columns[i] for i in selected_indices]
    except (ValueError, IndexError):
        print("Fehler: Ungültige Eingabe. Bitte nur gültige Spaltennummern verwenden.")
        exit(1)
    
    # Vorschau ausgeben
    print("\nAusgewählte Spalten (Stichprobe):\n")
    print(df[selected_columns].sample(5))
    
    # Optional speichern
    save = input("\nMöchtest du die Auswahl als CSV speichern? (j/n): ").strip().lower()
    if save == 'j':
        output_path = "auswahl.csv"
        df[selected_columns].to_csv(output_path, index=False)
        print(f"Datei gespeichert als '{output_path}'")

if __name__ == "__main__":
    main()