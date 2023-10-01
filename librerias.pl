% Librerias de programacion
% libreria(Nombre, Lenguaje, Uso, Descripcion)

libreria('pandas', 'python', 'data science',
'Con ella podemos leer archivos ó bases de datos de múltiples fuentes (csv, 
sqlite, sqlserver, html) y hacer operaciones entre las columnas, ordenar, 
agrupar, dividir, pivotar, totalizar. Nos ayuda a detectar valores nulos, 
detectar ouliers, duplicados y también hacer merge ó joins entre distintos 
orígenes. También nos permite guardar fácilmente nuestro nuevo dataset.').

libreria('numpy', 'python', 'data science',
'nos permite crear todo tipo de estructuras numéricas, múltiples dimensiones, 
permite transformarlas, operar aritméticamente, filtrar y es útil muchas veces 
para la inicialización de datos aleatorios.').

libreria('plotly', 'python', 'data science',
'con relativamente poco esfuerzo nos regala gráficas clicables, que nos aportan 
mayor información y nos ayudan en nuestra labor diaria.').

libreria('scikit learn', 'python', 'machine learning',
'Incluye varios algoritmos de clasificación, regresión y análisis de grupos entre 
los cuales están máquinas de vectores de soporte, bosques aleatorios, Gradient 
boosting, K-means y DBSCAN.').

% -------------------------------------------------------------------------------

% Predicado para obtener librerias dado el Lenguaje


libreria_de(Lenguaje, Nombre) :-
    libreria(Nombre, Lenguaje, _, _).