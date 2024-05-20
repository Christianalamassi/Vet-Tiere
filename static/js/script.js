const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let InfotId = e.target.getAttribute("Info_id");
        deleteConfirm.href = `delete_Info/${InfotId}`;
        deleteModal.show();
    });
}