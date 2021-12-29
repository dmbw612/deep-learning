def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"Type Error: {obj} is not {typer} type")

type_check(33, int)
type_check('string', str)