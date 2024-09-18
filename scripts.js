document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contractForm');
    const contractsList = document.getElementById('contractsList');

    form.addEventListener('submit', async function(event) {
        event.preventDefault();

        const formData = {
            contract_id: form.contractId.value,
            party_a: form.partyA.value,
            party_b: form.partyB.value,
            start_date: form.startDate.value,
            end_date: form.endDate.value,
            terms: form.terms.value,
        };

        const response = await fetch('/contracts', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });

        if (response.ok) {
            const contract = await response.json();
            displayContract(contract);
            form.reset();
        } else {
            console.error('Error creating contract');
        }
    });

    async function loadContracts() {
        const response = await fetch('/contracts');
        const contracts = await response.json();
        contracts.forEach(displayContract);
    }

    function displayContract(contract) {
        const div = document.createElement('div');
        div.className = 'contract';
        div.innerHTML = `
            <p><strong>Contract ID:</strong> ${contract.contract_id}</p>
            <p><strong>Party A:</strong> ${contract.party_a}</p>
            <p><strong>Party B:</strong> ${contract.party_b}</p>
            <p><strong>Start Date:</strong> ${contract.start_date}</p>
            <p><strong>End Date:</strong> ${contract.end_date}</p>
            <p><strong>Terms:</strong> ${contract.terms}</p>
        `;
        contractsList.appendChild(div);
    }

    loadContracts();
});
