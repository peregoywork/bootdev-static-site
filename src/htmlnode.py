class HTMLNode:
    def __init__(
            self, 
            tag: str | None = None, 
            value: str | None = None, 
            children: list['HTMLNode'] | None = None, 
            props: dict[str, str] | None = None,
        ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""
        return ' '.join([
            f'{k}="{v}"'
            for k,v in self.props.items()
        ])

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
            self, 
            tag: str | None, 
            value: str, 
            props: dict[str, str] | None = None,
        ):
        super().__init__(
            tag = tag,
            value = value,
            children = None, 
            props = props,
        )

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value, but this one is None")
        html_str = self.value
        if self.tag:
            html_str = f"<{self.tag}" + (f" {self.props}>" if self.props else ">") + html_str + f"</{self.tag}>"
        return html_str

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"






