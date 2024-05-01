export function formatCurrency(value) {
    return 'R$ ' + parseFloat(value).toFixed(2);
}

export function preventDotAndComma(event) {
    if (event.key === '.' || event.key === ',') {
        event.preventDefault();
    }
}