const tagDialog = document.getElementById('create-tag-form');
const postDialog = document.getElementById('create-post-form');
const tagInput = document.getElementById('tag-name');
const tagsContainer = document.getElementById('id_tags');
const createPostInput = document.getElementById('create-post-input');

let tagForm = null;
let contentTextarea = null;
let openPostButton = null;

if (tagDialog) {
    tagForm = tagDialog.querySelector('form');
}

if (postDialog) {
    contentTextarea = postDialog.querySelector('textarea[name="content"]');
}

if (createPostInput) {
    openPostButton = createPostInput.querySelector('button');
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
            syncTagsWithContent();
        }
    });

    if (openPostButton) {
        openPostButton.addEventListener('click', () => {
            syncTagsWithContent();
        });
    }

    openTagButton.addEventListener('click', () => {
        openTagDialog();
    });

    closeTagButton.addEventListener('click', () => {
        closeTagDialogAndReturn();
    });

    cancelTagButton.addEventListener('click', () => {
        closeTagDialogAndReturn();
    });

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
        syncTagsWithContent();
        closeTagDialogAndReturn();
    });
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

function syncTagsWithContent() {
    if (!contentTextarea) {
        return;
    }

    const previousTagsLine = contentTextarea.dataset.tagsLine || '';
    const tagsLine = getSelectedTagLabels().join(' ');
    let text = contentTextarea.value;

    if (previousTagsLine && text.endsWith(previousTagsLine)) {
        text = text.slice(0, -previousTagsLine.length).trimEnd();
    }

    if (tagsLine) {
        contentTextarea.value = `${text.trimEnd()}\n${tagsLine}`.trimStart();
    } else {
        contentTextarea.value = text;
    }

    contentTextarea.dataset.tagsLine = tagsLine;
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
