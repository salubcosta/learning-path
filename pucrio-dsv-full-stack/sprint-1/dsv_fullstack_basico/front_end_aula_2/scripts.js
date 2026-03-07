function addElemento(){
    const valor = document.getElementById("item").value;

    if(!valor){
        alert("Escreva o nome de algum item para adicionar à lista!");
        return;
    }

    const li = document.createElement("li");
    li.textContent = valor;

    li.onclick = editarItem;

    document.getElementById("minha-lista").appendChild(li);
    document.getElementById("item").value = "";
    document.getElementById("info").hidden = true;
    document.getElementById("item").focus();
}

function editarItem() {

    // Evita limpar o input caso ele exista dentra da li
    if (this.querySelector("input")) return;

    const textoAtual = this.textContent;

    const input = document.createElement("input");
    input.type = "text";
    input.value = textoAtual;
    input.style = "padding:5px;font-size:16px;";

    this.textContent = "";
    this.appendChild(input);

    input.focus();

    input.onblur = () => {
        this.textContent = input.value || textoAtual;
    };

    input.onkeydown = (e) => {
        if (e.key === "Enter") {
            input.blur();
        }
    };
}
