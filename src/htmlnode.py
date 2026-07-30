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
            html_str = f"<{self.tag}" + (f" {self.props_to_html()}>" if self.props else ">") + html_str + f"</{self.tag}>"
        return html_str

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(
        self, tag: str, children: list[HTMLNode], props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")
        if self.children is None:
            raise ValueError("invalid HTML: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"



