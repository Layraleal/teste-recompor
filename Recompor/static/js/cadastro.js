// Variável com o caminho base das imagens (deve estar na template Django)
  const caminhoBase = "{% static 'img/' %}";

  function abrirModal() {
    document.getElementById('modalFotos').style.display = 'flex';
  }

  function fecharModal() {
    document.getElementById('modalFotos').style.display = 'none';
  }

  function selecionarFoto(nomeFoto) {
    // Atualiza o input hidden
    document.getElementById('foto').value = nomeFoto;

    // Atualiza o preview com caminho completo
    const preview = document.getElementById('preview');
    preview.src = caminhoBase + nomeFoto;

    fecharModal();
  }