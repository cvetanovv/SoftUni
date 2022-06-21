window.addEventListener("load", solve);

function solve() {
    let titleElement = document.getElementById("post-title");
    let categoryElement = document.getElementById("post-category");
    let contentElement = document.getElementById("post-content");

    let publishBtn = document.getElementById("publish-btn");
    publishBtn.addEventListener("click", publish);

    function publish(event) {
        event.preventDefault();
        title = titleElement.value;
        category = categoryElement.value;
        content = contentElement.value;

        if(title === '' || category === '' || content === '') {
            return;
        }

        let reviewListsEl = document.getElementById('review-list');
        let postsContainerEl = document.createElement('li')
        postsContainerEl.className = "rpost"
        postsContainerEl.innerHTML = `<article>
                <h4>${title}</h4>

                <p>${category}</p>

                <p>${content}</p>
            </article>
            <button class="action-btn edit">Edit</button>
            <button class="action-btn approve">Approve</button>
        </li>`
        reviewListsEl.appendChild(postsContainerEl);
        let editBtn = postsContainerEl.querySelector(".edit")
        let ApproveBtn = postsContainerEl.querySelector(".approve")

        titleElement.value = ''
        categoryElement.value = ''
        contentElement.value = ''

        editBtn.addEventListener('click', edit);

        function edit(event) {
            event.preventDefault();

            titleElement.value = title
            categoryElement.value = category
            contentElement.value = content
            postsContainerEl.remove();
        }
        
        let uploadedPostsEl = document.getElementById('published-list');
        ApproveBtn.addEventListener('click', () => {
            uploadedPostsEl.appendChild(postsContainerEl)
            editBtn.remove();
            ApproveBtn.remove();
        })

        let clearButton = document.getElementById("clear-btn")
        clearButton.addEventListener('click', () => {
            uploadedPostsEl.innerHTML = '';
        })

    }
}
