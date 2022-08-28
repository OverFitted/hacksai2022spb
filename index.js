const {
    investing
} = require('investing-com-api');
const fs = require('fs');

async function main() {
    try {
        const response = await investing('currencies/usd-rub', 'MAX', 'P1M'); // With optional params

        for (const row in response) {
            if (Object.hasOwnProperty.call(response, row)) {
                response[row]["date"] /= 1000;
            }
        }

        fs.writeFileSync('res.json', JSON.stringify(response));
    } catch (err) {
        console.error(err);
    }
}

main()
