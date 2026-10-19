function myFunction() {
  enviarMensagemSeaTalk();
}

function enviarMensagemSeaTalk() {
  const WEBHOOK_URL = "https://openapi.seatalk.io/webhook/group/5mste44NTe6BKG2dm-SC0A";

const mensagem = [
  "🚨 **ATENÇÃO, EQUIPE DE TURNO!** 🚨",
  "",
  "⚠️ Antes de ligar as máquinas ou iniciar qualquer atividade, **FAÇA O SEU CHECK DE SEGURANÇA!**",
  "",
  "❤️ Sua vida e sua integridade vêm em 1º lugar. Não comece o turno sem garantir:",
  "",
  "🔒 **Cadeado LOTO + Chave:** Bloqueio é individual e obrigatório! Zero energia residual!",
  "🧤 **Luvas:** Proteja suas mãos contra cortes, prensamentos e queimaduras.",
  "🥽 **Óculos de Segurança:** Visão protegida durante todo o procedimento.",
  "",
  "🛑 Segurança não é opcional, é dever de todos.",
  "",
  "✅ Tenha um excelente e seguro turno de trabalho! 💪"
].join("\n");

  const payload = {
    tag: "text",
    text: {
      format: 1, // 1 = Markdown, 2 = texto puro
      content: mensagem
    }
  };

  const options = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload),
    muteHttpExceptions: true // permite ver o erro real no log
  };

  try {
    const response = UrlFetchApp.fetch(WEBHOOK_URL, options);
    Logger.log("Status: " + response.getResponseCode());
    Logger.log("Resposta do SeaTalk: " + response.getContentText());
  } catch (error) {
    Logger.log("Erro no envio: " + error.toString());
  }
}