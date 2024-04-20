# Ejercicios funciones

<dl>
        <dt>Ejercicio 1</dt>
        <dd>Crea un función EscribirCentrado, que reciba como parámetro un texto y lo escriba centrado en pantalla (suponiendo una anchura de 80 columnas; pista: deberás escribir 40 - longitud/2 espacios antes del texto). Además subraya el mensaje utilizando el carácter =.</dd>
        <dt>Ejercicio 2</dt>
        <dd>Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.</dd>
        <dt>Ejercicio 3</dt>
        <dd>Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal que, utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.</dd>
        <dt>Ejercicio 4</dt>
        <dd>Crea un función "ConvertirEspaciado", que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, "Hola, tú" devolverá "H o l a , t ú ". Crea un programa principal donde se use dicha función.</dd>
        <dt>Ejercicio 5</dt>
        <dd>Crea una función "calcularMaxMin" que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.</dd>
        <dt>Ejercicio 6</dt>
        <dd>Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.</dd>
        <dt>Ejercicio 7</dt>
        <dd>Crear una subrutina llamada "Login", que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es "usuario1" y la contraseña es "asdasd". Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.<br>
        Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.</dd>
        <dt>Ejercicio 8</dt>
        <dd>Crear una función recursiva que permita calcular el factorial de un número. Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.</dd>
         <dt>Ejercicio 9</dt>
    <dd>Crear una función que calcule el MCD de dos números por el método de Euclides. El método de Euclides es el siguiente:
        <ol>
            <li>Se divide el número mayor entre el menor.</li>
            <li>Si la división es exacta, el divisor es el MCD.</li>
            <li>Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.</li>
        </ol>
        Crea un programa principal que lea dos números enteros y muestre el MCD.</dd>
    <dt>Ejercicio 10</dt>
    <dd>Escribir dos funciones que permitan calcular:
        <ol>
            <li>La cantidad de segundos en un tiempo dado en horas, minutos y segundos.</li>
            <li>La cantidad de horas, minutos y segundos de un tiempo dado en segundos.</li>
        </ol>
        Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas, minutos y segundos o salir del programa.</dd>
    <dt>Ejercicio 11</dt>
    <dd>El día juliano correspondiente a una fecha es un número entero que indica los días que han transcurrido desde el 1 de enero del año indicado. Queremos crear un programa principal que al introducir una fecha nos diga el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:
        <ul>
            <li>LeerFecha: Nos permite leer por teclado una fecha (día, mes y año).</li>
            <li>DiasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.</li>
            <li>EsBisiesto: Recibe un año y nos dice si es bisiesto.</li>
            <li>Calcular_Dia_Juliano: Recibe una fecha y nos devuelve el día juliano.</li>
        </ul></dd>
    <dt>Ejercicio 12</dt>
    <dd>Vamos a mejorar el ejercicio anterior haciendo una función para validar la fecha. De tal forma que al leer una fecha se asegura que es válida.</dd>
    <dt>Ejercicio 13</dt>
    <dd>Queremos crear un programa que trabaje con fracciones a/b. Para representar una fracción vamos a utilizar dos enteros: numerador y denominador. Vamos a crear las siguientes funciones para trabajar con fracciones:
        <ul>
            <li>Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador. Cuando leas una fracción debes simplificarla.</li>
            <li>Escribir_fracción: Esta función escribe en pantalla la fracción. Si el denominador es 1, se muestra solo el numerador.</li>
            <li>Calcular_mcd: Esta función recibe dos números y devuelve el máximo común divisor.</li>
            <li>Simplificar_fracción: Esta función simplifica la fracción, dividiendo numerador y denominador por el MCD del numerador y denominador.</li>
            <li>Sumar_fracciones: Función que recibe dos fracciones n1/d1 y n2/d2, y calcula la suma de las dos fracciones. La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2. La fracción resultante debe simplificarse.</li>
            <li>Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2. La fracción resultante debe simplificarse.</li>
            <li>Multiplicar_fracciones: Función que recibe dos fracciones y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2. La fracción resultante debe simplificarse.</li>
            <li>Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente, para ello numerador=n1*d2 y denominador=d1*n2. La fracción resultante debe simplificarse.</li>
        </ul>
        Crea un programa que utilizando las funciones anteriores muestre el siguiente menú:
        <ul>
            <li>Sumar dos fracciones: En esta opción se piden dos fracciones y se muestra el resultado.</li>
            <li>Restar dos fracciones: En esta opción se piden dos fracciones y se muestra la resta.</li>
            <li>Multiplicar dos fracciones: En esta opción se piden dos fracciones y se muestra el producto.</li>
            <li>Dividir dos fracciones: En esta opción se piden dos fracciones y se muestra el cociente.</li>
            <li>Salir</li>
        </ul></dd>
        <dt>Ejercicio 14</dt>
    <dd>Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar.
        Para representar una pila vamos a utilizar una lista de cadenas de caracteres.
        Vamos a crear varias funciones para trabajar con la pila:
        <ul>
            <li>LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene.</li>
            <li>EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos.</li>
            <li>EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena.</li>
            <li>AddPila: Función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila si no está llena. Si está llena, muestra un mensaje de error.</li>
            <li>SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila. Si la pila está vacía, muestra un mensaje de error.</li>
            <li>EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila.</li>
        </ul>
        Realiza un programa principal que nos permita usar las funciones anteriores y que muestre un menú, con las siguientes opciones:
        <ol>
            <li>Añadir elemento a la pila</li>
            <li>Sacar elemento de la pila</li>
            <li>Longitud de la pila</li>
            <li>Mostrar pila</li>
            <li>Salir</li>
        </ol>
    </dd>
</dl>
