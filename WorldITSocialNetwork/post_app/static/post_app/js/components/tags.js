const tagDialog = document.getElementById('create-tag-form');
const tagForm = tagDialog?.querySelector('form');
const tagInput = document.getElementById('tag-name');
const tagsContainer = document.getElementById('id_tags');

const closeTagButton = document.getElementById('close-create-tag-form');
const cancelTagButton = document.getElementById('cancel-create-tag');
const saveTagButton = document.getElementById('save-create-tag');

if (tagDialog && tagForm && tagInput && tagsContainer) {
    const openTagButton = document.createElement('button');

    openTagButton.type = 'button';
    openTagButton.textContent = 'Додати хештег';

    tagsContainer.after(openTagButton);

    openTagButton.addEventListener('click', () => {
        tagInput.value = '';
        tagDialog.showModal();
        tagInput.focus();
    });

    closeTagButton?.addEventListener('click', () => {
        tagDialog.close();
    });

    cancelTagButton?.addEventListener('click', () => {
        tagDialog.close();
    });

    saveTagButton?.addEventListener('click', async () => {
        const formData = new FormData(tagForm);

        const response = await fetch(tagForm.action, {
            method: 'POST',
            body: formData,
        });

        const data = await response.json();

        addTagCheckbox(data.id, data.name);
        tagDialog.close();
    });
}

function addTagCheckbox(id, name) {
    const wrapper = document.createElement('div');
    const label = document.createElement('label');
    const checkbox = document.createElement('input');

    checkbox.type = 'checkbox';
    checkbox.name = 'tags';
    checkbox.value = id;
    checkbox.checked = true;
    checkbox.id = `id_tags_new_${id}`;

    label.htmlFor = checkbox.id;
    label.append(checkbox, ` #${name}`);

    wrapper.append(label);
    tagsContainer.append(wrapper);
}
