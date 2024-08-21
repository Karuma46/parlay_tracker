import { useEffect } from "react";

const Modal = ({ visible, hide, modal_id, title, children }) => {
  useEffect(() => {
    if (visible) {
      document.getElementById(modal_id).showModal();
    }
  }, [visible]);

  return (
    <>
      <dialog id={modal_id} className="modal">
        <div className="modal-box">
          <form method="dialog">
            <button
              className="btn btn-sm btn-circle btn-ghost absolute right-2 top-2"
              onClick={hide}>
              ✕
            </button>
          </form>
          <h3 className="font-bold text-lg">{title}</h3>
          <div className="pt-6">{children}</div>
        </div>
      </dialog>
    </>
  );
};

export default Modal;
