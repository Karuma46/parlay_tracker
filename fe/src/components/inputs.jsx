import Icon from "./icons";

export const TextInput = (props) => {
  return (
    <label
      className={`input input-bordered flex items-center gap-2 ${props?.className} outline-none`}
      placeholder={props?.placeholder}>
      <Icon icon={props?.icon} size="xs" />
      <input
        type={props?.type || "text"}
        className="w-full bg-none text-sm pl-2"
        placeholder={props?.placeholder}
        value={props?.value}
        onChange={props?.onChange}
      />
    </label>
  );
};
