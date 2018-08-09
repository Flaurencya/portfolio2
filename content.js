chrome.runtime.onMessage.addListener(
function(request, sender, sendResponse) {
    if(request.message === "vocab_word" ) {
      //gets highlighted word
      var selected = (window.getSelection().toString()).split(" ");
      alert(selected);
      selected = document.getElementById("definition").string;
      //inputting the selected word into the API
      var query = "https://owlbot.info/api/v2/dictionary/"+ selected;
      var request = new XMLHttpRequest();
      request.open('GET', api/v2/dictionary/selected);
      request.send();
      var requestInformation = JSON.parse(definition)
      var full = selected + "means: " + requestInformation
      alert(full);
      }
}
);
