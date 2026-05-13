const tagDialog = document.getElementById('create-tag-form');
const postDialog = document.getElementById('create-post-form');
const tagInput = document.getElementById('tag-name');
const tagsContainer = document.getElementById('id_tags');

let tagForm = null;
let contentTextarea = null;
const mainTagsSpan = document.createElement('span');

if (tagDialog) {
    tagForm = tagDialog.querySelector('form');
}

if (postDialog) {
    contentTextarea = postDialog.querySelector('textarea[name="content"]');
}

if (contentTextarea) {
    createContentField();
    resizeContentTextarea();

    contentTextarea.addEventListener('input', () => {
        resizeContentTextarea();
    });
}

const closeTagButton = document.getElementById('close-create-tag-form');
const cancelTagButton = document.getElementById('cancel-create-tag');
const saveTagButton = document.getElementById('save-create-tag');

let openTagButton = null;

if (tagDialog && tagForm && tagInput && tagsContainer) {
    openTagButton = document.createElement('button');

    openTagButton.type = 'button';
    openTagButton.textContent = '+';
    openTagButton.classList.add('add-tag-button');
    openTagButton.setAttribute('aria-label', 'Add hashtag');

    tagsContainer.append(openTagButton);

    tagsContainer.addEventListener('change', (event) => {
        if (event.target.matches('input[name="tags"]')) {
            syncTagsSpan();
        }
    });

    openTagButton.addEventListener('click', () => {
        openTagDialog();
    });

    if (closeTagButton) {
        closeTagButton.addEventListener('click', () => {
            closeTagDialogAndReturn();
        });
    }

    if (cancelTagButton) {
        cancelTagButton.addEventListener('click', () => {
            closeTagDialogAndReturn();
        });
    }

    if (saveTagButton) {
        saveTagButton.addEventListener('click', async () => {
            const formData = new FormData(tagForm);

            const response = await fetch(tagForm.action, {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();

            if (!response.ok) {
                return;
            }

            addTagCheckbox(data.id, data.name);
            syncTagsSpan();
            closeTagDialogAndReturn();
        });
    }
}

function openTagDialog() {
    tagInput.value = '';

    if (postDialog && postDialog.open) {
        postDialog.close();
    }

    tagDialog.showModal();
    tagInput.focus();
}

function closeTagDialogAndReturn() {
    if (tagDialog.open) {
        tagDialog.close();
    }

    if (postDialog && !postDialog.open) {
        postDialog.showModal();
    }
}

function syncTagsSpan() {
    mainTagsSpan.textContent = getSelectedTagLabels().join(' ');

    if (mainTagsSpan.textContent) {
        mainTagsSpan.hidden = false;
    } else {
        mainTagsSpan.hidden = true;
    }
}

function createContentField() {
    const contentField = document.createElement('div');

    contentField.classList.add('content-field');
    contentTextarea.rows = 1;
    contentTextarea.parentNode.insertBefore(contentField, contentTextarea);
    contentField.append(contentTextarea);

    mainTagsSpan.classList.add('content-tag');
    mainTagsSpan.hidden = true;
    contentField.append(mainTagsSpan);

    contentField.addEventListener('click', () => {
        contentTextarea.focus();
    });
}

function resizeContentTextarea() {
    contentTextarea.style.height = 'auto';
    contentTextarea.style.height = `${contentTextarea.scrollHeight}px`;
}

function getSelectedTagLabels() {
    const checkedTags = tagsContainer.querySelectorAll('input[name="tags"]:checked');
    const tagLabels = [];

    checkedTags.forEach((checkbox) => {
        const tagLabel = getTagLabel(checkbox);

        if (tagLabel) {
            tagLabels.push(tagLabel);
        }
    });

    return tagLabels;
}

function getTagLabel(checkbox) {
    const label = checkbox.closest('label') || tagsContainer.querySelector(`label[for="${checkbox.id}"]`);

    if (!label) {
        return '';
    }

    const text = label.textContent.trim();

    if (!text) {
        return '';
    }

    if (text.startsWith('#')) {
        return text;
    } else {
        return `#${text}`;
    }
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

    if (openTagButton) {
        tagsContainer.insertBefore(wrapper, openTagButton);
    } else {
        tagsContainer.append(wrapper);
    }
}
