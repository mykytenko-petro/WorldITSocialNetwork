export function filterContacts(contacts) {
    const ukrainianAlphabet = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
    const englishAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    const filteredContacts = {}

    for (const letter of ukrainianAlphabet) {
        filteredContacts[letter] = []
    }

    for (const letter of englishAlphabet) {
        filteredContacts[letter] = []
    }

    filteredContacts["#"] = []

    const ukrainianPattern = /^[А-ЩЬЮЯҐЄІЇа-щьюяґєії]/
    const englishPattern = /^[A-Za-z]/

    for (const contact of contacts) {
        const name = contact.pseudonym
        if (!name) continue

        const firstChar = name[0].toUpperCase()

        if (ukrainianPattern.test(firstChar)) {
            filteredContacts[firstChar].push(contact)
        } else if (englishPattern.test(firstChar)) {
            filteredContacts[firstChar].push(contact)
        } else {
            filteredContacts["#"].push(contact)
        }
    }

    const cleanedContacts = Object.fromEntries(
        Object.entries(filteredContacts).filter(([key, value]) => value.length > 0)
    )

    return cleanedContacts
}

export function filterContactsFlat(contacts) {
    return Object.values(filterContacts(contacts)).flat()
}