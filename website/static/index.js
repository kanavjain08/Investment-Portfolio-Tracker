function deleteItem(stockId) {
    fetch('/delete-stock', {
        method: 'POST',
        body: JSON.stringify({ stockId: stockId })
    }).then((_res) => {
        window.location.href = "/";
    })
}