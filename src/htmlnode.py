class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        try:
            pass
        except:
            raise NotImplementedError("to_html not implemented")
    
    def props_to_html(self):
        return f"{self.props}"