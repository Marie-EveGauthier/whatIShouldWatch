<?php

/* TutoTestBundle:Default:writerview.html.twig */
class __TwigTemplate_ad00150f9036da5d7a3be4c31f7a41e88f773941530b3229d56c3093395373a2 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = $this->env->loadTemplate("::base.html.twig");

        $this->blocks = array(
            'body' => array($this, 'block_body'),
        );
    }

    protected function doGetParent(array $context)
    {
        return "::base.html.twig";
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        $this->parent->display($context, array_merge($this->blocks, $blocks));
    }

    // line 3
    public function block_body($context, array $blocks = array())
    {
        $context['_parent'] = (array) $context;
        $context['_seq'] = twig_ensure_traversable((isset($context["writer"]) ? $context["writer"] : $this->getContext($context, "writer")));
        foreach ($context['_seq'] as $context["_key"] => $context["w"]) {
            // line 4
            echo "        ";
            echo twig_escape_filter($this->env, $this->getAttribute((isset($context["w"]) ? $context["w"] : $this->getContext($context, "w")), "id"), "html", null, true);
            echo "
";
        }
        $_parent = $context['_parent'];
        unset($context['_seq'], $context['_iterated'], $context['_key'], $context['w'], $context['_parent'], $context['loop']);
        $context = array_intersect_key($context, $_parent) + $_parent;
    }

    public function getTemplateName()
    {
        return "TutoTestBundle:Default:writerview.html.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  34 => 4,  28 => 3,);
    }
}
