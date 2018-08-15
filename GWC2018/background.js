// chrome.contentMenus.onClicked.addListener(function(info, tab) {
//     if (info.menuItemId == "vocab_word") {
//         chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
//           chrome.tabs.sendMessage(tabs[0].id, {"message": "vocab_word"});
//   };
//   };
// };

chrome.contextMenus.create({
    "title": "Add to WordCatcher",
    "id": "vocab_word",
    "contexts": ["all"]
});

chrome.contextMenus.onClicked.addListener(function (info, tab) {
    if (info.menuItemId == "vocab_word") {
        chrome.tabs.query({active: true, currentWindow: true}, function (tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {"message": "vocab_word"});
        });
    }
});
