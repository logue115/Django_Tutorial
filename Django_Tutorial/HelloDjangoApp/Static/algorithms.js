// JavaScript source code
var array1 = [];

function Array_Gen() {
    var i;
    for (i = 0; i < 5; i++) {
        array1[i] = Math.round(Math.random() * 100);
    }
    var A2 = array1;
    A2.toString();
    document.getElementById("Original_Array").innerHTML = A2;
}

function Insertion_Sort() {
    var i, j, key;

    for (j = 1; j < array1.length; j++) {
        key = array1[j];
        i = j - 1;
        while (i >= 0 && array1[i] > key) {
            array1[i + 1] = array1[i];
            i = i - 1;
        }
        array1[i + 1] = key;

    }
    array1.toString();
    document.getElementById("Sorted_Array").innerHTML = array1;
}