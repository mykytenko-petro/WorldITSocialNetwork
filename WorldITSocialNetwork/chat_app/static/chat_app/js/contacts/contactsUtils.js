export function filterContacts(contacts) {
    const ukrainianAlphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ";
    const englishAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    const filteredContacts = new Map();

    for (const letter of ukrainianAlphabet) {
        filteredContacts.set(letter, []);
    }

    for (const letter of englishAlphabet) {
        filteredContacts.set(letter, []);
    }

    filteredContacts.set("#", []);

    const ukrainianPattern = /^[А-ЩЬЮЯҐЄІЇа-щьюяґєії]/;
    const englishPattern = /^[A-Za-z]/;

    for (const contact of contacts) {
        const name = contact.pseudonym;
        if (!name) continue;

        const firstChar = name[0].toUpperCase();

        if (ukrainianPattern.test(firstChar)) {
            filteredContacts.get(firstChar).push(contact);
        } else if (englishPattern.test(firstChar)) {
            filteredContacts.get(firstChar).push(contact);
        } else {
            filteredContacts.get("#").push(contact);
        }
    }

    const cleanedContacts = new Map(
        [...filteredContacts.entries()].filter(([key, value]) => value.length > 0)
    );

    return cleanedContacts;
}

export function filterContactsFlat(contacts) {
    return [...contacts.values()].flat()
}