<?php
// Verifica se um comando foi enviado pelo formulário
if (isset($_POST['comando'])) {
	// Obtém o comando enviado
	$comando = $_POST['comando'];

	// Executa o comando no Raspberry Pi
	exec($comando, $saida, $status);

	// Verifica se o comando foi executado com sucesso
	if ($status == 0) {
		echo "Comando executado com sucesso!";
	} else {
		echo "Erro ao executar o comando: " . implode("\n", $saida);
	}
}