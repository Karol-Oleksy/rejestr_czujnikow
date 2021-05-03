-------------------------------------
OPIS PROJEKTU
-------------------------------------

  Projekt jest implementacją serwisu udostępniającego JSON REST API, które pozwola na zarządzanie czujnikami jakości powietrza poprzez: dodawanie czujników, edycję czujników, usuwanie czujników i pobieranie czujników.
  
-------------------------------------
SPOSÓB KORZYSTANIA Z ENDPOINTÓW
-------------------------------------

  Aby uruchomić aplikację, należy (po uprzednim pobraniu plików) uruchomić skrypt w pliku 'main.py'. Jeśli skrypt uruchamia się poprawnie, należy w przeglądarce internetowej przejść do adresu Localhost (http://127.0.0.1:5000/). Pod podstawowym adresem uruchomi się główna strona serwisu.
  
  Na głównej stronie są dostępne 3 hiperłącza do poszczególnych funkcji serwisu.
  
  -> Dodaj czujnik
  
    Ta funkcja pozwala na dodanie czujnika. Hiperłącze przekierowuje do formularza, w którym należy uzupełnić wszystkie dane czujnika (imię i nazwisko właściciela oraz adres czujnika, składający się z ulicy, numeru ulicy, kodu pocztowego, miejscowości oraz kraju). Po kliknięciu 'Zapisz' czujnik zostaje zapisany, oraz zostaje nadany mu wyróżniający go identyfikator.
  
  -> Wyświetl/edytuj/usuń czujnik
  
    Pod tą pozycją kryją się trzy funkcje Hiperłącze przekierowuje do formularza, w którym należy podać id czujnika. Następnie należy wybrać (za pomocą umieszczonych poniżej przycisków) akcję, która zostanie wykonana:
    
    - Wyświetl
      
      Serwis wyświetla dane czujnika w formacie JSON.
      
    - Edytuj
    
      Przekierowuje do formularza, w którym można zmienić aktualne dane czujnika. Jedynie id jest daną tylko do odczytu.
      
    - Usuń
    
      Usuwa czujnik z pamięci aplikacji.
      
  -> Wyświetl wszystkie czujniki
  
    Ta funkcja pozwala na wyświetlenie listy danych wszystkich czujników w formacie JSON.
    
