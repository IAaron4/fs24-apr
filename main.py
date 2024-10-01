def max_subarray(arr):
    # Variablen initialisieren
    max_sum = 0  # Maximale gefundene Summe
    current_sum = 0  # Aktuelle Teilsumme
    start = end = temp_start = 0  # Indizes für das beste Intervall

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start  # Intervall neu setzen
            end = i

        # Wenn die aktuelle Teilsumme negativ ist, setzen wir sie auf 0
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1  # Neuer möglicher Startpunkt

    return max_sum, start, end


if __name__ == '__main__':
    kursverlauf = [31, -41, 59, 26, -53, 58, 97, -93, -23]
    gewinn, start_index, end_index = max_subarray(kursverlauf)

    print(f"Maximaler Gewinn: {gewinn}")
    print(f"Start-Index: {start_index}, End-Index: {end_index}")

# Laufzeit-Analyse

# Der Kadane-Algorithmus hat eine Zeitkomplexität von O(n), da die Liste nur einmal durchlaufen wird.

# Wenn die Länge der Liste verdoppelt wird, wird die Laufzeit ebenfalls ungefähr verdoppelt. Dies bedeutet, dass der Algorithmus sehr effizient ist, auch für große Eingaben.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

